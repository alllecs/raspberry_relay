#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define SYSFS_GPIO_DIR "/sys/class/gpio"

#define INPUT	0
#define OUTPUT	1

#define BUT1 25
#define BUT2 24
#define BUT3 23
#define BUT4 18
#define BUT5 12
#define BUT6 16
#define BUT7 20
#define BUT8 21

#define NROW 4
#define NCOL 4

static
int gpioExport(int gpio) {
	int fd, len, ret = -1;
	char buf[255];

	fd = open(SYSFS_GPIO_DIR "/export", O_WRONLY);
	if (fd) {
		len = snprintf(buf, sizeof(buf), "%d", gpio);
		write(fd, buf, len);
		close(fd);
		ret = 0;
	}

	return ret;
}

static
int gpioSetDirection(int gpio, int direction) {
	int fd, len, ret = -1;
	char buf[255];

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/direction", gpio);
	fd = open(buf, O_WRONLY);
	
	if (fd) {
		if (direction) {
			write(fd, "out", 3);
		}
		else {
			write(fd, "in", 2);
		}
		close(fd);
		ret = 0;
	}

	return ret;
}

static
int gpioOpen(int gpio) {
	char buf[255];

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/value", gpio);

	return open(buf, O_WRONLY);
}

static
void gpioSet(int gpio_fd, int value) {
	if (gpio_fd) {
		if (value) {
			write(gpio_fd, "1", 2);
		}
		else {
			write(gpio_fd, "0", 2);
		}
	}
}

static
int gpioGet(int gpio) {
	int n, v;
	FILE *fd;
	char buf[255];

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/value", gpio);
	fd = fopen(buf, O_RDONLY);
	if (fd == NULL) {
		perror("Error open file");
		return 2;
	}

	n = fscanf(fd, "%d", &v);
	if (n != 1) {
		printf("Error read file\n");
	}
	fclose(fd);

	return v;
}

int main(void) {
	int row[NROW] = { BUT1, BUT2, BUT3, BUT4 };
	int row_fd[NROW]; 
	int col[NCOL] = { BUT5, BUT6, BUT7, BUT8 }; 
	int col_fd[NCOL];
	char *names[NROW][NCOL] = {

		{ "S1", "S2", "S3", "S4" },
		{ "S5", "S6", "S7", "S8" },
		{ "S9", "S10", "S11", "S12" },
		{ "S13", "S14", "S15", "S16" },
	};

//	assign_name(row, col, "S7");

//	printf("(2, 1) = %s\n", );
//	return;

	for(int i=0;i<NROW;i++) {
		gpioExport(row[i]);
		gpioSetDirection(row[i], 1);
		gpioSet(row[i], 0);
		for(int j=0;j<NCOL;j++) {
			gpioExport(col[j]);
			gpioSetDirection(col[j], 0);
			*names[i][j] = gpioGet(col[j]);
			printf("%s\t", names[i][j]);
		}
		gpioSet(row[i], 1);
		printf("\n");
	}

	return 0;
}

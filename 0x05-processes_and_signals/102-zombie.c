#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - looops indefinetely to keep the mains process active
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 * main - runs the code
 * Return: Exit status of 0
 */
int main(void)
{
	int x = 0;
	pid_t pid;

	while (x < 5)
	{
		pid = fork();

		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			x++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}

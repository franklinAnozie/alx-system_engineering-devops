#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - an infinity while loop. Keeps main running
 * Return: Always returns 0.
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
 * pid_creator - recursively creates childreb processes as long
 * as the count value isn't equal to 5
 * @count: keeps track of the count that stops the recursion
*/
void pid_creator(int count)
{
	pid_t pid;

	if (count >= 5)
		return;

	pid = fork();
	if (pid == 0)
	{
		exit(EXIT_SUCCESS);
	}
	else
	{
		printf("Zombie process created, PID: %d\n", pid);
		pid_creator(++count);
	}
}

/**
 * main - Runs an infinite loop, thereby making sure parent
 * process never closes its children processes, thereby
 * creating 5 zombie processes
 * Return: Always returns 0.
*/
int main(void)
{
	int i = 0;

	pid_creator(i);
	infinite_while();
	return (0);
}

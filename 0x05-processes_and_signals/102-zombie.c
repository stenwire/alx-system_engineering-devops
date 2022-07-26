#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - runs an infinite while loop
 * Return: integer
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
 * main - Entry point
 * Return: 0 on success
 */
int main(void)
{
	int i, ZOMBIE_PID;

	for (i = 0; i < 5; i++)
	{
		ZOMBIE_PID = fork();
		if (ZOMBIE_PID > 0)
			printf("Zombie process created, PID: %d\n", ZOMBIE_PID);
		else
			break;
	}

	if (ZOMBIE_PID != 0)
		infinite_while();

	return (0);
}
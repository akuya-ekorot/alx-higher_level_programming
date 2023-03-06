#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of singly linked list
 * Return: return 0 if there's no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *current;
	int i, j;

	current = list;
	i = 0;

	while(current)
	{
		if (i != 0)
		{
			temp = list;
			j = 0;
			while (j < i)
			{
				if (temp == current)
					return (1);

				j++;
				temp = temp->next;
			}
		}
		current = current->next;
		i++;
	}

	return (0);
}

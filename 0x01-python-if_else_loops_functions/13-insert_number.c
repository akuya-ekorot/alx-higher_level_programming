#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the first node in the list
 * @number: number to insert in the list
 *
 * Return: Address of the new node, NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr, *next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	/* empty list */
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	/* insert at the begining */
	if ((*head)->n <= new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	curr = *head;
	next = (*head)->next;

	while(next)
	{
		if (new->n >= curr->n && new->n < next->n)
		{
			if (next->next)
				new->next = next;
			else
				new->next = NULL;

			curr->next = new;
			break;
		}
		else
		{
			curr = curr->next;
			next = next->next;
		}
	}
	return (new);
}

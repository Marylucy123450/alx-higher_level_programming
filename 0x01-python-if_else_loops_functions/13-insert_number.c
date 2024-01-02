#include "lists.h"

/**
 *insert_node - Inserts a number into a sorted singly-linked list
 *@head: A pointer the head of the linked list
 *@number: The number to insert
 *
 *Return: NULL in case of failure
 *	a pointer to the new mode
 */
listint_t *insert_node(listint_t **head, int number)
{
	/* Allocate memory for the new node. */
	listint_t *new_node = malloc(sizeof(listint_t));

	/* Initialize a pointer to traverse the list. */
	listint_t *current = *head;

	/* Check if memory allocation was successful. */
	if (new_node == NULL)
		return (NULL);

	/* Set the value of the new node. */
	new_node->n = number;
	new_node->next = NULL;

	/* Check if the list is empty or the new node should be the new head. */
	if (*head == NULL || number < current->n)
	{
		/* Make the new node the new head. */
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the correct position for the new node. */
	while (current->next != NULL)
	{
		if (number >= current->n && number <= current->next->n)
		{
			/* Insert the new node between current and current->next. */
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}

	/* If the new node belongs at the end, add it there. */
	current->next = new_node;
	return (new_node);
}

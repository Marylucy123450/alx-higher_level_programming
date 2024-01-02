#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;/* Declare a pointer to a listint_t structure. */
	unsigned int n; /*  Declare an unsigned integer n to count nodes. */

	current = h; /* Set 'current' to point to the head of the list 'h'. */
	n = 0; /*  Initialize the count of nodes to 0. */

	/*Iterate through the list until the current node is */
	/*NULL (end of the list). */
	while (current != NULL)
	{
		printf("%i\n", current->n);  /*Print the 'n' (data) of the current node. */
		current = current->next; /*Move 'current' to the next node in the list. */
		n++;    /*  Increment the count of nodes. */
	}

	return (n);  /* Return the total number of nodes in the list. */
}


/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in the new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new; /*Declare pointer to listint_t structure represent new node*/

	/*Allocate memory for a new listint_t node using malloc. */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);  /* If malloc fails, return NULL to indicate failure. */
	/* Set the 'n' (data) of the new node to the value passed as an argument*/
	new->n = n;
	/* Set the 'next' pointer of the new node to the current head of list*/
	new->next = *head;
	*head = new;  /* Update the head of the list to point to the new node. */

	return (new);  /* Return the address of the new node to indicate success. */
}


/**
 * free_listint - frees a listint_t list
 * @head: pointer to the list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;  /* Declare a pointer to listint_t called 'current'. */

	/* Start a loop that continues as long as 'head' is not NULL */
	/*(the list is not empty). */
	while (head != NULL)
	{
		/* Assign value of 'head' to 'current', which is temporary pointer. */
		current = head;
		head = head->next; /*  Move 'head' to the next node in the list.
				    */
		free(current);  /* Free the memory allocated for the 'current' node. */
	}
}

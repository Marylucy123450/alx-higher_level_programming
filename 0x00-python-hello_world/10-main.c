#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;  /* // Declare a pointer to listint_t called 'head'. */
	listint_t *current; /*  // Declare a pointer to listint_t called 'current'. */
	listint_t *temp;  /* // Declare a pointer to listint_t called 'temp'. */
	int i; /*  // Declare an integer variable 'i'. */

	head = NULL;  /*Initialize 'head' pointer to NULL,indicating an empty list*/
	/* // Add nodes to the linked list using the 'add_nodeint' function. */
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 1024);
	/* // Print the elements of the linked list. */
	print_listint(head);
	/*Check if the linked list has a cycle using the 'check_cycle' function. */
	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");
	/* // Create a cycle in the linked list. */
	current = head;  /* // Initialize 'current' to point to the head. */
	for (i = 0; i < 4; i++)
		current = current->next;  /* // Move 'current' four nodes forward. */
	temp = current->next;  /* // Store node to be connected for creating cycle. */
	current->next = head;  /* // Connect last node to head, creating a cycle. */
	if (check_cycle(head) == 0)/*Check if the linked list has a cycle again. */
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");
	/* // Restore the linked list to its original state by breaking the cycle. */
	current = head;  /* // Initialize 'current' again to the head. */
	for (i = 0; i < 4; i++)
		current = current->next;  /* // Move 'current' four nodes forward. */
	current->next = temp;  /*Break cycle by reconnecting last node to 'temp'*/
	/* // Free the memory used by the linked list. */
	free_listint(head);
	return (0);
}

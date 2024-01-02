#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list; /* Initialize slow pointer to head of the list. */
	listint_t *fast = list;  /* Initialize a fast pointer to head of the list.*/

	if (list == NULL)
		return (0);  /* If list is empty (NULL), there's no cycle, so return 0. */

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;        /* Move the slow pointer by one step */
		fast = fast->next->next;  /* Move the fast pointer by two steps */

		/* If there's a cycle, the slow and fast pointers will meet at some point. */
		if (slow == fast)
			return (1);  /* Return 1 to indicate that a cycle was found. */
	}
    /* If the loop terminates without the pointers meeting, there's no cycle,*/
    /*so return 0. */

	return (0);
}

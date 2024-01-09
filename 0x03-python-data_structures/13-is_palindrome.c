#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL; /*pointer to reverse the first half of the list */
	listint_t *temp;           /* Temporary pointer */

    /* An empty list or a list with only one element is a palindrome */
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (fast != NULL && fast->next != NULL)
	{
		/* Move fast two steps and slow one step */
		fast = fast->next->next;

		/* Reverse the first half of the list */
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
    /* If the list has an odd number of elements, adjust slow */
	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev != NULL)
	{
		if (prev->n != slow->n)
			return (0);  /* It's not a palindrome */

		prev = prev->next;
		slow = slow->next;
	}

	return (1);  /* It's a palindrome */
}

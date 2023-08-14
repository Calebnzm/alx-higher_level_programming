#include "lists.h"
#define LARGE 10000

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: begining of the linked list
*
* Return: (0) not palindrome (1) is palindrome
*/
int is_palindrome(listint_t **head)
{
	int i, j, array[LARGE];
	listint_t *current = *head;

	i = j = 0;

	if (*head == NULL)
	{
		return (1);
	}
	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	for (j = 0; j < i / 2; j++)
	{
		if (array[j] == array[i - 1 - j])
		{
			continue;
		}
		else
		{
			return (0);
		}
		i--;
	}
	return (1);
}

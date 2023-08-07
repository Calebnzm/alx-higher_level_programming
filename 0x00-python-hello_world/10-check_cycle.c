#include "lists.h"

/**
* check_cycle - checks if a linked list has a cycle
* @list: pointer to the head of the linked list
*
* Return: (0) if no cycle, (1) if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (list == NULL)
	{
		return (0);
	}
	hare = tortoise = list;
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == tortoise)
		{
			return (1);
		}
	}
	return (0);
}

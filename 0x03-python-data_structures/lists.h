#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
replace_in_list(my_list, idx, element);
print_reversed_list_integer(my_list=[]);
new_in_list(my_list, idx, element);
print_matrix_integer(matrix=[[]]);
add_tuple(tuple_a=(), tuple_b=());

int is_palindrome(listint_t **head);

#endif /* LISTS_H */

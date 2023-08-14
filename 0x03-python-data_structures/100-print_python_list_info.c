#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - prints some onfo about python lists
* @p: pointer
*
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	const char *type;
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		*type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}

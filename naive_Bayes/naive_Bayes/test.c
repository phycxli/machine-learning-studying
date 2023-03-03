#include<stdio.h>

int sort(int a[])
{
	int n = sizeof(a);
	return a;
}

int main()
{
	int a[] = { 4,3,5,1,7 };
	int* b = sort(a);
	printf("%p",*b);

	return 0;
} 
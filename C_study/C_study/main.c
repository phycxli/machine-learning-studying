#include<stdio.h>

int main()
{
	char a[] = { 0,1,2,3,4,5,6 ,-1 };
	char* p = a;
	while (*p != -1)
	{
		printf("%d\n",*p++);
	}
}
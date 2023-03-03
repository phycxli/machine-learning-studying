#include<stdio.h>
#define sunny 0
#define overcast 1
#define rainy 2
#define hot 0
#define mild 1
#define cool 2
#define high 0
#define normal 1
#define f 0
#define t 1
#define no 0
#define yes 1

int sort(int a[]);

int main()
{
	int outlook[] = { sunny, sunny, overcast, rainy, rainy, rainy, overcast, sunny, sunny, rainy, sunny, overcast, overcast, rainy };
	int temperature[] = { hot, hot, hot, mild, cool, cool, cool, mild, cool, mild, mild, mild, hot, mild };
	int humdity[] = { high, high, high, high, normal, normal, normal, high, normal, normal, normal, high, normal, high };
	int windy[] = { f, t, f, f, f, t, t, f, f, f, t, t, f, t };
	int play[] = { no, no, yes, yes, yes, no, yes, no, yes, yes, yes, yes, yes, no };
	int* a = sort(outlook);
	int i;
	for (i = 0; i < 14; i++)
	{
		print("%d\n",a[i]);
	}
	return 0;
}


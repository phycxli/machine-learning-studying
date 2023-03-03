#include<stdio.h>

double inner(double x[2], double y[2])
{
	int i;
	double sum = 0;
	for (i = 0; i < 2; i++)
	{
		sum += x[i] * y[i];
	}
	return sum;
}
int main()
{
	double x[3][2] = { {3,3},{4,3},{1,1} };
	int y[3] = { 1,1,-1 };
	double gram[3][3];
	int i = 0;
	int j = 0;
	for (i=0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			gram[i][j] = inner(x[i], x[j]);
		}
	}
	printf("The Gram matrix:\n%lf %lf %lf\n%lf %lf %lf\n%lf %lf %lf\n", gram[0][0], gram[0][1], gram[0][2], gram[1][0], gram[1][1], gram[1][2], gram[2][0], gram[2][1], gram[2][2]);
	double a[3] = { 0,0,0 };
	double b = 0;
	double lr = 1;
	for (i = 0; i < 3;)
	{
		int j = 0;
		int sum = 0;
		for (j = 0; j < 3; j++)
		{
			sum += a[j] * y[j] * gram[j][i];
		}
		if (y[i] * (sum + b) <= 0)
		{
			a[i] = a[i] + lr;
			b = b + lr * y[i];
			printf("incorrect point:x%d,update parameters:a0 %lf\ta1 %lf\ta2 %lf\tb,%lf\n", i+1, a[0], a[1], a[2], b);
			i = 0;
		}
		else
		{
			i++;
		}
	}
	double w[2] = { 0,0 };
	for (i = 0; i < 2; i++)
	{
		int j = 0; 
		for (j = 0; j < 3; j++)
		{
			w[i] += a[j] *y[j]* x[j][i];
		}
	}
	printf("hyper surface:%lf x[1]+%lf x[2]+%lf\n", w[0], w[1], b);
	printf("Please enter point:");
	double x1, x2;
	scanf_s("%lf,%lf",&x1,&x2);
	if (w[0] * x1 + w[1] * x2 + b >0)
	{
		printf("1");
	}
	else
	{
		printf("-1");
	}
	return 0;
}
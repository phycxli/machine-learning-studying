#include<stdio.h>
//train data points
int main()
{
	int x[3][2];
	x[0][0] = 3;
	x[0][1] = 3;
	x[1][0] = 4;
	x[1][1] = 3;
	x[2][0] = 1;
	x[2][1] = 1;
	int y[3];
	y[0] = 1;
	y[1] = 1;
	y[2] = -1;
	double w[2];
	w[0] = 0;
	w[1] = 0;
	double b = 0;
	int i = 0;
	for (i = 0; i < 3; i++)
	{
		if (y[i] * (w[0] * x[i][0] + w[1] * x[i][1] + b) <= 0)
		{
			w[0] = w[0] + y[i] * x[i][0];
			w[1] = w[1] + y[i] * x[i][0];
			b = b + y[i];
			i = 0;
			printf("times %d,parameters:%lf,%lf,%lf\n",i,w[0],w[1],b);
		}
	}
	printf("hyper-surface: %lf x1+%lf x2+%lf", w[0], w[1], b);
	return 0;
}
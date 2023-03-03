#include <stdio.h>
#include<math.h>


double func(double x, double y)
{
	double z = 0;
	z = pow(pow(x, 2) + pow(y, 2), 2) - 4 * (pow(x, 2) + pow(y, 2));
	return z;
}
int main()
{
	double eps;
	eps = 0.01;
	int i;
	double x=2, y=2, l=0.01;
	double z0, z1;
	for (i = 0; i < 10000; i++)
	{
		z0 = func(x, y);
		x = x - 2 * x * l * i;
		y = y - 2 * y * l * i;
		z1 = func(x, y);
		if (z1 > z0)
		{
			break;
		}
	}
	printf("%lf,%lf", x, y);
	return 0;
}

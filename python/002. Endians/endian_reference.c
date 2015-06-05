#include <stdio.h>

unsigned long conv_endian(unsigned long x)
{
	unsigned long t = x;

	x = ((x>>8) | (x & 0x000000ff) << 24) & 0xff00ff00;
	t = ((t<<8) | (t & 0xff000000) >> 24) & 0x00ff00ff;

	return (x | t);
}

int main()
{
	unsigned long x = 4294967295;//2018915346//1//100000/4294967295
	unsigned long y = conv_endian(x);

	return 0;
}
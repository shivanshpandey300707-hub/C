 #include <stdio.h>

int main(void)
{
	int score;

	scanf("%d", &score);

	if (score >= 40)
	{
		if (score >= 75)
		{
			printf("Classification: Excellent\n");
		}
		else
		{
			printf("Classification: Good\n");
		}
	}
	else
	{
		printf("Classification: Fail\n");
	}

	return 0;
}

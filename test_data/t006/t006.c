
int calc(int a, int b) {
    
    int c;
    
    if (a > 7) {
        c = a + b;
	    return c;
    }
    
    c = a * b;
    return c;
}

int main() {
	int c = calc(5, 7);
	for (int i = 0; i < 5; i++)
		c++;
}


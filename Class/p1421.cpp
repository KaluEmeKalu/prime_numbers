#include <bits/stdc++.h>
using namespace std;

int n1, n2, ans;

int main() {
	scanf("%d %d", &n1, &n2);
	for (int i = n1; i <= n2; ++i) {
		if (i % 4 == 0 || i % 2) {
			ans++;
		}
	}
	printf("%d", ans);
}

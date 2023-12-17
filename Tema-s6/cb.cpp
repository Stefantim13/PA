#include <bits/stdc++.h>
using namespace std;
int v[100];

void cauta(int st, int dr, int x)
{
    int mij;
    while(st <= dr)
    {
        mij = (st + dr) / 2;
        if(v[mij] < x)
            st = mij + 1;
        else
            dr = mij - 1;
    }
    if(v[st] == x)
        return st;
    else
        return -1;
}


int main()
{
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i)
		cin >> v[i];
	sort(v + 1, v + n + 1);
	cin >> x;
	cauta(x);
	return 0;
}

#include<iostream>
#define MAX 20
using namespace std;

int R, C;
char arr[MAX][MAX];
int alphabet[26];
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
int maxpath = 0;

void dfs(int row, int col, int path);

int main(int argc, char** argv)
{
	cin >> R >> C;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> arr[i][j];
		}
	}
	alphabet[((int)arr[0][0]) - 65]++;
	dfs(0, 0, 1);
	cout << maxpath << "\n";
	return 0;
}

void dfs(int row, int col, int path)
{
	if (path > maxpath) maxpath = path;
	for (int dir = 0; dir < 4; dir++)
	{
		int nx = row + dx[dir];
		int ny = col + dy[dir];

		if (0 <= nx && nx < R && 0 <= ny && ny < C)
		{
			if (!alphabet[((int)arr[nx][ny]) - 65])
			{
				alphabet[((int)arr[nx][ny]) - 65]++;
				dfs(nx, ny, path + 1);
				alphabet[((int)arr[nx][ny]) - 65]--;
			}
		}
	}
}
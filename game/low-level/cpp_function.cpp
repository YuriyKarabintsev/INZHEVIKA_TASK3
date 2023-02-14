#include <iostream>
#include <string>
#include <vector>
using namespace std;

void get_possible_moves(int xchip, int ychip, string direction,
    int distance, vector<pair<int, int> >& result) {

    if (result.empty())
        result = vector<pair<int, int> >();
    vector<pair<int, int> > possible_moves = vector<pair<int, int> >();

    if ((xchip > 7 || xchip < 0) || (ychip > 7 || ychip < 0)) {
        result.insert(result.end(), possible_moves.begin(), possible_moves.end());
    }

    if (direction == "down") {
        int i = 0;
        while (ychip != ychip - distance && 0 <= ychip && ychip <= 7) {
            if (0 <= xchip - (distance - i) && xchip - (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair((xchip - distance + i), ychip));
            }

            if (0 <= xchip + (distance - i) && xchip + (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair((xchip + distance - i), ychip));
            }
            i++;
            ychip++;
        }
    }
    else if (direction == "up") {
        int i = 0;
        while (ychip != ychip + distance && 0 <= ychip && ychip <= 7) {
            if (0 <= xchip - (distance - i) && xchip - (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair((xchip - distance + i), ychip));
            }

            if (0 <= xchip + (distance - i) && xchip + (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair((xchip + distance - i), ychip));
            }
            i++;
            ychip--;
        }
    }
    else if (direction == "left") {
        int i = 0;
        while (xchip != xchip - distance && 0 <= xchip && xchip <= 7) {
            if (0 <= ychip - (distance - i) && ychip - (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair(xchip, ychip - (distance - i)));
            }

            if (0 <= ychip + (distance - i) && ychip + (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair(xchip, ychip + (distance - i)));
            }
            i++;
            xchip++;
        }
    }
    else {
        int i = 0;
        while (xchip != xchip + distance && 0 <= xchip && xchip <= 7) {
            if (0 <= ychip - (distance - i) && ychip - (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair(xchip, ychip - (distance - i)));
            }

            if (0 <= ychip + (distance - i) && ychip + (distance - i) <= 7 && distance - i >= 0) {
                possible_moves.__emplace_back(make_pair(xchip, ychip + (distance - i)));
            }
            i++;
            xchip--;
        }
    }

    result.insert(result.end(), possible_moves.begin(), possible_moves.end());
}

int main() {

    vector<pair<int, int> > result = vector<pair<int, int> >();

    get_possible_moves(0, 0, "down", 1, result);

    for (size_t i = 0; i < result.size(); i++)
    {
        cout << result[i].first << " - " << result[i].second << endl;
    }
}
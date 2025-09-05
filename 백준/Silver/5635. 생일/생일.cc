#include <iostream>
#include <string>

using namespace std;

struct person
{
    string name;
    int day;
    int month;
    int year;
};

person youngest_person(person p1, person p2) {
    if (p1.year != p2.year) {
        return (p1.year > p2.year) ? p1 : p2;
    } else if (p1.month != p2.month) {
        return (p1.month > p2.month) ? p1 : p2;
    } else {
        return (p1.day > p2.day) ? p1 : p2;
    }
}

person oldest_person(person p1, person p2) {
    if (p1.year != p2.year) {
        return (p1.year < p2.year) ? p1 : p2;
    } else if (p1.month != p2.month) {
        return (p1.month < p2.month) ? p1 : p2;
    } else {
        return (p1.day < p2.day) ? p1 : p2;
    }
}

int main() {
    int count_people;
    cin >> count_people;

    person youngest, oldest;
    for (int i=0; i<count_people; i++) {
        string name;
        int day, month, year;
        cin >> name >> day >> month >> year;
        
        if (i==0) {
            youngest = {name, day, month, year};
            oldest = {name, day, month, year};
        } else {
            person current = {name, day, month, year};
            youngest = youngest_person(youngest, current);
            oldest = oldest_person(oldest, current);
        }
    }
    cout << youngest.name << "\n" << oldest.name;
}
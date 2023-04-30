#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    // return value
    string militaryTime = s;

    // get hours as integer
    string hoursString = s.substr(0, 2);
    int hoursInt = stoi(hoursString);

    // get AM or PM suffix
    string ampm = s.substr(s.length()-2, s.length());
    if(ampm == "AM") {
        // 12 AM is 0 military time
        if(hoursInt == 12) {
            hoursInt = 0;
        }
    }
    else if(ampm == "PM") {
        // add 12 to convert to military time
        if(hoursInt != 12) {
            hoursInt += 12;
        }
    }
    string hoursStringMilitary = to_string(hoursInt);
    if(hoursStringMilitary.length() == 1) {
        hoursStringMilitary = "0" + hoursStringMilitary;
    }
    militaryTime = militaryTime.replace(0, 2, hoursStringMilitary);

    // remove AM or PM suffix (needed for both AM and PM conversion)
    militaryTime = militaryTime.substr(0, militaryTime.length()-2);

    return militaryTime;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}

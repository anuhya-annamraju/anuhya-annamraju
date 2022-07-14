/******************************************************************************

Problem : Given an array of positive integers, find the longest sequence of sub-array
possible containing ascending numbers in ascending order. The numbers dont have to be
contigious.

Author : Anuhya Annamraju
Date : 14-07-2022 

*******************************************************************************/

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    //vector<int> input = {1,3,4,6,2,11,15,19,25,21,45,33,29,55,63};
    vector<int> input = { 1,2,3,4,6,11,15,23,47,19,21,25,45 };
    int largest = 0, max = 0;
    int index_i = 0, index_j = 0;

    for (int i = 0; i < input.size(); i++)
    {
        if (input.at(i) > max)
        {
            max = input.at(i);
        }
    }


    while (index_i < input.size())
    {
        index_j = index_i;
        int prev = -1;
        vector<int> miss, sequence;
        cout << "\n";
        while (index_j < input.size())
        {
            int curr_val = input.at(index_j);

            if (curr_val == max)
            {
                sequence.push_back(max);
                index_j++;
                break;
            }

            if (curr_val > prev)
            {
                sequence.push_back(curr_val);
                prev = curr_val;
            }

            else
            {
                miss.push_back(index_j);
            }

            index_j++;
        }


        if (miss.size() != 0)
        {
            index_i = miss.at(0);
        }
        else
        {
            index_i = index_j;
        }

        for (int i = 0; i < sequence.size(); i++)
        {
            cout << sequence.at(i) << " ";
        }


        if (sequence.size() > largest)
        {
            largest = sequence.size();
        }


        if (input.size() - index_j <= largest)
        {
            cout << " \n All the sequences after this will be shorter than the largest sequence. Hence Breaking. \n";
            index_i = input.size();
        }

    }
    cout << "Largest sequence Lenght :: " << largest;

    return 0;
}

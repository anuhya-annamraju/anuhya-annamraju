
using System;
using System.Collections.Generic;

class Sorter
{

    public List<int> QuickSort(List<int> subArray)
    {
        List<int> left = new List<int>();
        List<int> right = new List<int>();
        List<int> sorted = new List<int>();
        if (subArray.Count > 0)
        {
            int pivot = subArray[subArray.Count - 1];
            for (int i = 0; i < subArray.Count - 1; i++)
            {
                if (subArray[i] < pivot)
                {
                    left.Add(subArray[i]);
                }
                else
                {
                    right.Add(subArray[i]);
                }
            }

            sorted = QuickSort(left);
            sorted.Add(pivot);
            sorted.AddRange(QuickSort(right));
        }

        return sorted;
    }
}
public class Executer
{
    public static void Main(string[] args)
    {
        List<int> arr = new List<int> { 9, -3, 5, 2, 6, 8, -6, 1, 3 };
        Sorter h = new Sorter();
        List<int> sorted = h.QuickSort(arr);

        foreach (var v in sorted)
        {

            Console.WriteLine(v + ", ");
        }
    }
}
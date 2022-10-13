using System;
using System.Collections.Generic;

 class Sorter
{
    public List<int> BubbleSort(List<int> arr)
    {
        for (int i = 0; i < arr.Count  ; i++)
        {
            for (int j = 0 ; j < arr.Count - i - 1; j++ )
            {
                if (arr[j] > arr[j + 1])
                {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
            foreach(var v in arr)
            {
                Console.WriteLine(v+"");
            }
            Console.WriteLine("............................");
        }
        
        return arr;
    }
    
}
public class Executer
{
    public static void Main(string[] args)
    {
        List<int> arr = new List<int>{9,-3,5,2,6,8,-6,1,3};
        Sorter h = new Sorter();
        List<int> sorted = h.BubbleSort(arr);
        
        foreach (var v in sorted)
        {
            Console.WriteLine (v + ",");
        }
    }

}
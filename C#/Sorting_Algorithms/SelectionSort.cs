using System;
using System.Collections.Generic;

 class Sorter
{
    public List<int> SelectionSort(List<int> arr)
    {
        for (int i = 0; i< arr.Count ; i++)
        {
            int smallest = i;
            int j ;
            
            Console.WriteLine("Smaller before: "+ arr[smallest]);
            for(j = i +1 ; j< arr.Count ; j++)
            {
                if (arr[j] < arr[smallest])
                {
                    smallest = j;
                }
            }
            
            Console.WriteLine("Smaller now: "+ arr[smallest]);
            if (smallest != i)
            {
                int temp = arr[i];
                arr[i] = arr[smallest];
                arr[smallest] = temp;
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
        Sorter sorter = new Sorter();
        List<int> sorted = sorter.SelectionSort(arr);
        
        foreach (var v in sorted)
        {
            Console.WriteLine (v + ",");
        }
    }

}
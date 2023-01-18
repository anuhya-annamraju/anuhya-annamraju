using System;
using System.Threading.Tasks;

namespace Async_Await_Tas
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Task coffee = MakeCoffee();
            Task boilEggs = BoilEggs();
            Task plates = PreparePlateAndGlass();

            await Task.WhenAll(coffee, boilEggs, plates);
            Console.WriteLine("Breakfast is ready");
            Console.ReadKey();
        }

        static async Task MakeCoffee()
        {
            Console.WriteLine("Making Coffee in the Coffee machine");
            await Task.Delay(4000);
        }

        static async Task BoilWaterForEggs()
        {
            Console.WriteLine("Boiling Water");
            await Task.Delay(4000);
            Console.WriteLine("Water is boiled");
        }

        static async Task PreparePlateAndGlass()
        {
            Console.WriteLine("Washing and wiping plate & glass");
            await Task.Delay(4000);
            Console.WriteLine("Plate & glass are ready");
        }

        static async Task BoilEggs()
        {
            await BoilWaterForEggs();
            Console.WriteLine("Adding eggs");
            await Task.Delay(2000);
            Console.WriteLine("Eggs are Boiled");
        }
        
    }
}


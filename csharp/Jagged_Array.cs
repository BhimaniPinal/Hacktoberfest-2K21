using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Jacked_Arrays
{
    class Program
    {
        static void Main(string[] args)
        {
            // the program will make jagged arrays having a main(parent) array of length 2 and sub (child) array of any length specified by user
            int x;
            Console.WriteLine("How many subjects are there in your result");
            x = Convert.ToInt32(Console.ReadLine());
            // jagged array has been declared
            string[][] result = new string[2][];
            // child arrays will be declared here now 
            result[0] = new string[x]; // this array will hold the names of the subjects
            result[1] = new string[x]; // this array will hold the marks of the subjects
            // now its time to populate the array
            string values; // this variable will get values from user later on which will be inserted in arrays
            for(int i=0; i < 2; i++)
            {
                for(int j=0; j<x; j++)
                {
                    if (i == 1)
                    {
                        Console.WriteLine("Enter marks for: " + result[0][j]);
                        values = Console.ReadLine();
                        result[i][j] = values;
                    }
                    else
                    {
                        Console.WriteLine("Enter Subject " + (j + 1) + " name");
                        values = Console.ReadLine();
                        result[i][j] = values;

                    }
                    
                }               
            }
            Console.WriteLine("\t\t\t===========================================================\t\t\t");
            Console.WriteLine("Result is:");
            // integer 'ii' is used to point to the child arrays of the main array "result"
            int ii = 0;            
            //for loop for iterating through the values of the second child array that holds "marks"
                for (int jj = 0; jj < x; jj++)
                {
                    Console.WriteLine("Subject:" + result[ii][jj]);
                    Console.WriteLine("Marks: " + result[(ii+1)][jj]);
                }
        }
    }
}

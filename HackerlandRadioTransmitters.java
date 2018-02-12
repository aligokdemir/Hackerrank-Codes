//Link to the challenge: 
//https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int partition(int[] x, int low, int high){
        int pivot = x[high];
        int i = (low-1);
        for(int j = low; j < high; j++){
            if(x[j] <= pivot){
                i++;
                
                //swap
                int temp = x[i];
                x[i] = x[j];
                x[j] = temp;
            }
        }
        
        int temp = x[i+1];
        x[i+1] = x[high];
        x[high] = temp;
        
        return i+1;
    }
    
    static void sort(int x[], int low, int high){
        if(low < high){
            int partitionIndex = partition(x, low, high);
            
            sort(x, low, partitionIndex - 1);
            sort(x, partitionIndex + 1, high);
        }
    }
    
    static int hackerlandRadioTransmitters(int[] x, int k, int n) {
        int numberOfTransmitters = 0;
        int i = 0;
        while(i < n){
            numberOfTransmitters++;
            int location = x[i] + k;
            while(i < n && x[i] <= location) i++;
            location = x[--i] + k;
            while(i < n && x[i] <=location) i++;
        }
        return numberOfTransmitters;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] x = new int[n];
        for(int x_i = 0; x_i < n; x_i++){
            x[x_i] = in.nextInt();
        }
        sort(x, 0, n - 1);
        int result = hackerlandRadioTransmitters(x, k, n);
        System.out.println(result);
        in.close();
    }
}

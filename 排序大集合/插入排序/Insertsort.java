import java.util.Arrays;

public class Insertsort {
	
	
	public static void insertSort(int[] arr) {
		if (arr == null || arr.length < 2) {
			return;
		}
		for (int i = 0; i < arr.length-1; i++) {
			int minIndex = i; 
			for (int j=i+1; j<arr.length; j++) {
				minIndex = arr[j] < arr[minIndex] ? j: minIndex;
			}
			swap(arr, i, minIndex);
		}	
	}
	public static void swap(int[] arr, int i, int j ) {
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
	
	
	
	public static void main(String[] args) {
		int[] text = {10,3,4,7,8,9,1,5};
		System.out.println("Before sorted" + Arrays.toString(text));
		insertSort(text);
		System.out.println("After sorted" + Arrays.toString(text));
		
		
		
	}

}

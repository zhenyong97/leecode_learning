import java.util.Arrays;

public class BubbleSort {
	
	public static void bubbleSort(int[] arr) {
		if (arr == null || arr.length < 2) {
			return ;
		}
		/* 每遍历完一次，数组长度都会减一 */
		for (int e = arr.length - 1; e > 0; e--) { 
			for (int i = 0; i < e; i++) {
				if (arr[i] > arr[i + 1]) {
					swap(arr, i, i + 1);
				}
			}
		}
	}

	public static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] array = {9,1,8,3,5,2,6};
		System.out.println("冒泡排序前"+ Arrays.toString(array));
		bubbleSort(array);
		System.out.println("冒泡排序后"+ Arrays.toString(array));
		

	}

}

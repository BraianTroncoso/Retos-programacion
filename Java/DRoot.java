// Digital root is the recursive sum of all the digits in a number.
// Given n, take the sum of the digits of n. If that value has more than one digit, 
//continue reducing in this way until a single-digit number is produced. 
//The input will be a non-negative integer.

// Examples
//     16  -->  1 + 6 = 7
//    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
// 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
// 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
public class DRoot {
    public static int digital_root(int n) {
        // Iteramos sobre el número y sumamos los dígitos
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        
        // Si la suma tiene más de un dígito, llamamos recursivamente a la función con la suma
        if (sum > 9) {
            return digital_root(sum);
        } else {
            return sum; // Retornamos la suma si tiene un solo dígito
        }
    }

    public static void main(String[] args) {
        // Ejemplo de uso:
        int result = digital_root(9876);
        System.out.println("Raíz digital: " + result);
    }
}

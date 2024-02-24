// Write a function that takes an integer as input, and returns the number of bits that are equal
// to one in the binary representation of that number. You can guarantee that input is non-negative.
// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

public class BitCounting {

    public static int countBits(int n) {
        String binary = Integer.toBinaryString(n);
        int count = 0;
        for (char bit : binary.toCharArray()) {
            if (bit == '1') {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // Ejemplo de uso:
        int bits = countBits(1234);
        System.out.println("Cantidad de bits activos en 1234: " + bits);
    }
}

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class AdivinaPalabra {
    public static void main(String[] args) {
        ArrayList<String> words = new ArrayList<>();
        words.add("braian");
        words.add("java");
        words.add("corazon");

        Random random = new Random();
        String word = words.get(random.nextInt(words.size()));

        int hiddenLetters = (int) (word.length() * 0.6);
        ArrayList<Integer> hiddenPositions = new ArrayList<>();
        for (int i = 0; i < hiddenLetters; i++) {
            int randomPosition;
            do {
                randomPosition = random.nextInt(word.length());
            } while (hiddenPositions.contains(randomPosition));
            hiddenPositions.add(randomPosition);
        }

        StringBuilder hiddenWord = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            hiddenWord.append(hiddenPositions.contains(i) ? "_" : word.charAt(i));
        }

        int attempts = 5;
        Scanner scanner = new Scanner(System.in);

        while (attempts > 0) {
            System.out.println("Adivina la palabra: " + hiddenWord);
            System.out.println("Tienes " + attempts + " intentos.");

            String input = scanner.nextLine();

            if (input.length() == 1) {
                boolean success = false;
                StringBuilder newHiddenWord = new StringBuilder();

                for (int i = 0; i < word.length(); i++) {
                    if (input.charAt(0) == word.charAt(i) && hiddenWord.charAt(i) == '_') {
                        newHiddenWord.append(input.charAt(0));
                        success = true;
                    } else {
                        newHiddenWord.append(hiddenWord.charAt(i));
                    }
                }

                hiddenWord = newHiddenWord;

                if (success) {
                    if (word.equals(hiddenWord.toString())) {
                        System.out.println("¡Has acertado! La palabra oculta era: " + word);
                        break;
                    } else {
                        System.out.println("Has acertado la letra!");
                    }
                } else {
                    System.out.println("Letra no encontrada.");
                    attempts--;
                }
            } else if (input.length() == word.length()) {
                if (input.equals(word)) {
                    System.out.println("¡Has acertado! La palabra oculta era: " + word);
                    break;
                } else {
                    System.out.println("La palabra no es correcta.");
                    attempts--;
                }
            } else {
                System.out.println("Texto invalido.");
            }
        }

        if (attempts == 0) {
            System.out.println("Has perdido. La palabra correcta era " + word + ".");
        }
    }
}

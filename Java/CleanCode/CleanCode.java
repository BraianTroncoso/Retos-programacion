import java.util.ArrayList;
import java.util.List;

public class CleanCode{
    public static void main(String[] args) {

        // Usar nombres que revelen las intenciones 1)

        // public List<Cell> getFlaggedCells() {
        //     List<Cell> flaggedCells = new ArrayList<Cell>();
        //     for (Cell cell : gameBoard)
        //     if (cell.isFlagged())
        //     flaggedCells.add(cell);
        //     return flaggedCells;
        //     }

        // Realizar distinciones con sentido 2)

        // Los nombres tienen que ser mas descriptivos y tienen que ser notablemente diferentes
        // Aca abajo ejemplo de como NO se debe hacer
        // public static void copyChars(char a1[], char a2[]) {
        // for (int i = 0; i < a1.length; i++) {
        //         a2[i] = a1[i];
        //     }
        // }
        //     getActiveAccount();
        //     getActiveAccounts();
        //     getActiveAccountInfo();

        // Usar nombres que se puedan pronunciar 3)

        // Compare:
        // class DtaRcrd102 {
        // private Date genymdhms;
        // private Date modymdhms;
        // private final String pszqint = “102”;
        // /*… */
        // };
        // con:
        // class Customer {
        // private Date generationTimestamp;
        // private Date modificationTimestamp;
        // private final String recordId = “102”;
        // /*… */
        // };


        // Usar nombres que se puedan buscar

        // Compare:
        // for (int j=0; j<34; j++) {
        // s += (t[j]*4)/5;
        // }
        // con:
        // int realDaysPerIdealDay = 4;
        // const int WORK_DAYS_PER_WEEK = 5;
        // int sum = 0;
        // for (int j = 0; j < NUMBER_OF_TASKS; j++) {
        // int realTaskDays = taskEstimate[j] * realDaysPerIdealDay;
        // int realTaskWeeks = (realdays / WORK_DAYS_PER_WEEK);
        // sum += realTaskWeeks;
}
            
    
    }

import java.util.ArrayList;
import java.util.List;

public class CleanCode{
    public static void main(String[] args) {

        // Usar nombres que revelen las intenciones
        public List<Cell> getFlaggedCells() {
            List<Cell> flaggedCells = new ArrayList<Cell>();
            for (Cell cell : gameBoard)
            if (cell.isFlagged())
            flaggedCells.add(cell);
            return flaggedCells;
            }
    }
}
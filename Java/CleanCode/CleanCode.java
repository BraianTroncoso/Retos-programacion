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


        // Usar nombres que se puedan buscar 4)

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
        // Evitar codificaciones 5)
        
        // Ya tenemos suficientes codificaciones como para tener que añadir otras
        // nuevas. Al codificar información de tipos o ámbitos en un nombre se dificulta
        // la descodificación. No parece razonable que todos los nuevos empleados
        // tengan que aprender otro lenguaje de codificación además del código con el
        // que van a trabajar. Es una carga mental innecesaria a la hora de intentar
        // solucionar un problema. Los nombres codificados resultan impronunciables y
        // suelen escribirse de forma incorrecta.
    

        // Notación húngara 6)

        // PhoneNumber phoneString;
        // El nombre no cambia cuando cambia el tipo


        // Prefijos de miembros 7)

        // public class Part {
        //     private String m_dsc; // La descripción textual
        //     void setName(String name) {
        //     m_dsc = name;
        //     }
        //     }
        //     public class Part {
        //     String description;
        //     void setDescription(String description) {
        //     this.description = description;
        //     }
        //     }


        // Interfaces e Implementaciones 8)

        // ¿Qué nombres debe
        // asignar? ¿IShapeFactory y ShapeFactory? Prefiero las interfaces sin
        // adornos. La I inicial, tan habitual en los archivos de legado actuales es, en el
        // mejor de los casos, una distracción, y en el peor, un exceso de información.
        // No quiero que mis usuarios sepan que se trata de una interfaz, solamente que
        // se trata de ShapeFactory. Si tengo que codificar la interfaz o la
        // implementación, opto por ésta última. Es mejor usar ShapeFactoryImp o
        // incluso CShapeFactory, que codificar la interfaz.


        // Evitar asignaciones mentales 9)

        // No hay peor motivo para usar el nombre c que a y b ya estén
        // seleccionados.
        // Por lo general, los programadores son gente inteligente. A la gente
        // inteligente le gusta presumir de sus habilidades mentales. Si puede recordar
        // que r es la versión en minúscula de una URL sin el host y el sistema, debe ser
        // muy listo.
        // Una diferencia entre un programador inteligente y un programador
        // profesional es que este último sabe que la claridad es lo que importa. Los
        // profesionales usan sus poderes para hacer el bien y crean código que otros
        // puedan entender.


        // Nombres de clases 10)

        // Las clases y los objetos deben tener nombres o frases de nombre como
        // Customer, WikiPage, Account y AddressParser. Evite palabras como
        // Manager, Processor, Data, o Info en el nombre de una clase. El nombre de
        // una clase no debe ser un verbo.


        // Nombre de métodos 11)
        
        // Los métodos deben tener nombres de verbo como postPayment, deletePage
        // o save. Los métodos de acceso, de modificación y los predicados deben tener
        // como nombre su valor y usar como prefijo get, set e is de acuerdo al
        // estándar de javabean[9].
        // string name = employee.getName();
        // customer.setName(“mike”);
        // if (paycheck.isPosted())…
        // Al sobrecargar constructores, use métodos de factoría estáticos con
        // nombres que describan los argumentos. Por ejemplo:
        // Complex fulcrumPoint = Complex.FromRealNumber(23.0);
        // es mejor que:
        // Complex fulcrumPoint = new Complex(23.0);
        // Refuerce su
        // correspondientes.
        // uso
        // convirtiendo
        // en
        // privados
        // sus
        // constructores


        // No se exceda con el atractivo 12)

        // Opte por la claridad antes que
        // por el entretenimiento. En el código, el atractivo suele aparecer como formas
        // coloquiales o jergas. Por ejemplo, no use whack() en lugar de kill(). No
        // recurra a bromas culturales como eatMyShorts() si quiere decir abort().
        // Diga lo que piense. Piense lo que diga.
    

        // Una palabra por concepto 13)

        // Elija una palabra por cada concepto abstracto y manténgala. Por ejemplo,
        // resulta confuso usar fetch, retrieve y get como métodos equivalentes de
        // clases distintas. ¿Cómo va a recordar qué método se corresponde a cada
        // clase?

        // No haga juegos de palabras 14)

        // Evite usar la misma palabra con dos fines distintos. Suele hacerse en juegos
        // de palabras. Si aplica la regla de una palabra por conceptos, acabará con
        // muchas clases que por ejemplo tengan un método add. Mientras las listas de
        // parámetros y los valores devueltos de los distintos métodos add sean
        // semánticamente equivalentes, no hay problema.


        // Usar nombres de dominios de soluciones 15)
    }

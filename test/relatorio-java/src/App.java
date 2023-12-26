import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class App {
    public static void main(String[] args) {
        String filePath = "./data/Exp04_Aceleracao_da_gravidade_local.csv";
        String delimiter = " ; ";

        List<String[]> data = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] columns = line.split(delimiter);
                data.add(columns);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Agora você pode manipular o array 'data' conforme necessário
        for (String[] row : data) {
            System.out.println(Arrays.toString(row));
        }
    }
}

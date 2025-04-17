package com.example.greenhouse;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {
    private TextView tempText, humidText, lightText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tempText = findViewById(R.id.temp_text);
        humidText = findViewById(R.id.humid_text);
        lightText = findViewById(R.id.light_text);

        ApiService api = NetworkService.getInstance().getApi();

        api.getSensorData().enqueue(new Callback<SensorData>() {
            @Override
            public void onResponse(Call<SensorData> call, Response<SensorData> response) {
                SensorData data = response.body();
                if (data != null) {
                    tempText.setText("Температура: " + data.getTemperature() + "°C");
                    humidText.setText("Влажность: " + data.getHumidity() + "%");
                    lightText.setText("Освещённость: " + data.getLight() + "лк");
                }
            }

            @Override
            public void onFailure(Call<SensorData> call, Throwable t) {
                tempText.setText("Ошибка загрузки данных");
            }
        });
    }
}
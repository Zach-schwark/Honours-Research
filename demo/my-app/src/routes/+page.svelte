<script lang='ts'>
    
    type LoanStructure = {
        int_rate : string ,
        loan_amnt: string,
        installment: string,
        term: string
    }
    
    
    //const API_URL = import.meta.env.PROD 
    //    ? 'https://honours-research.vercel.app'
    //    : 'http://localhost:8000';

    let inputValues = {};
    let prediction : LoanStructure = {int_rate : "",
        loan_amnt: "",
        installment: "",
        term: "" };


    let error: any = null;

    async function getPrediction() {
        try {
            const response = await fetch('https://honours-research.vercel.app/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    variables: inputValues
                })
            });
            
            if (!response.ok) {
                throw new Error('Prediction failed');
            }
            
            const data = await response.json();
            prediction.int_rate = data.prediction.int_rate;
            prediction.loan_amnt = data.prediction.loan_amnt;
            prediction.installment = data.prediction.installment;
            prediction.term = data.prediction.term;
            console.log(prediction)
            error = null;
        } catch (err) {
            error = 'Failed to get prediction';
            console.error(err);
        }
    }
</script>

<form on:submit|preventDefault={getPrediction}>
    <!-- Your input fields here -->
    <button type="submit">Get Prediction</button>
</form>

{#if prediction}
    <div class="prediction">
        Interest Rate: {prediction.int_rate}<br>
        Loan Amount: {prediction.loan_amnt}<br>
        Installment Amount: {prediction.installment}<br>
        Loan Term: {prediction.term}<br>
    </div>
{/if}

{#if error}
    <div class="error">
        {error}
    </div>
{/if}
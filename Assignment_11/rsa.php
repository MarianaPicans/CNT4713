<?php
//constant to connect to the database
define('DB_NAME', 'rsa');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_HOST', 'localhost');

//action: 'encrypt' or 'decrypt' and the string will be the value entered by the user
function encrypt_decrypt($action, $string) {
    $output = false;
    $encrypt_method = "AES-256-CBC";
    $secret_key = 'This is my secret key';
    $secret_iv = 'This is my secret iv';
    // hash value 
    $key = hash('sha256', $secret_key);
    
    // iv - encrypt method AES-256-CBC expects 16 bytes - else you will get a warning
    $iv = substr(hash('sha256', $secret_iv), 0, 16);
    if ( $action == 'encrypt' ) {
        $output = openssl_encrypt($string, $encrypt_method, $key, 0, $iv);
        $output = base64_encode($output);
    } else if( $action == 'decrypt' ) {
        $output = openssl_decrypt(base64_decode($string), $encrypt_method, $key, 0, $iv);
    }
    return $output;
}

//connect to db and check connection was successful 
$link = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD);

if(!$link){
	die('Could not connect: ' . mysqli_error($link));
}

$db_selected = mysqli_select_db($link, DB_NAME);

if(!$db_selected) {
	die('Can\'t use ' . DB_NAME . ': ' . mysqli_error($link));
}

//grab values entered by the user from the form
$encryptedValue = $_POST["encrypted"];
$decryptedValue = $_POST["decrypted"];

//check if the text entered by the user was encrypted text or plain text
if($_POST["encrypted"] == ""){
    //decrypting encrypted text entered by the user
    $encryptedValue = $_POST["decrypted"];
    $decryptedValue = encrypt_decrypt("decrypt",$encryptedValue);
}else{
//encrypting the plain text etered by the user
$encryptedValue = encrypt_decrypt("encrypt",$encryptedValue);

//this should match original text entered bythe user
$decryptedValue = encrypt_decrypt("decrypt",$encryptedValue);
}

//inserting the values into the database and checking that the connection worked and the query was successful
$sql = "INSERT INTO rsa_tabe (encryption, decryption) VALUES ('$encryptedValue','$decryptedValue')";

if (!mysqli_query($link, $sql)){
	die('Error: ' . mysqli_error($link));
}
//retrieving the information from the database to desplay it 
$query  = "SELECT * FROM rsa_tabe WHERE encryption = '$encryptedValue'";
$result = mysqli_query($link, $query);
if($result){
    $row = mysqli_fetch_array($result);
}else{
    die('Error: ' . mysqli_error($link));
}

mysqli_close($link);
?>

<form action="rsaform.php" method = "post"/>
<p>Encrypted Text: <input type="text" name="decrypted" value="<?php echo $row['encryption'];?>"/></p>
<p>Decrypted Text: <input type="text" name="encrypted" value="<?php echo $row['decryption'];?>"/></p>
<input type="submit" value="Encrypt and Decrypt more text"/>
</form>
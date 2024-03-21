<?php

require 'vendor/autoload.php'; // Include the Composer autoload file

use Aws\S3\S3Client;

// Specify your AWS region and S3 bucket name
$bucket = 'your-s3-bucket-name';
$prefix = 'space/accounts/'; // The folder path within your S3 bucket where result.html is located

// Instantiate the S3 client
$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'your-aws-region',
]);

try {
    // Get the result.html template content from S3
    $result = $s3->getObject([
        'Bucket' => $bucket,
        'Key'    => $prefix . 'result.html', // Concatenate the prefix and file name
    ]);

    // Output the content of the template
    echo $result['Body'];
} catch (Aws\Exception\S3Exception $e) {
    // If there is an error retrieving the object
    echo "Error getting email template: " . $e->getMessage();
}

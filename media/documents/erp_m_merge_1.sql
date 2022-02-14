-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2020 at 01:44 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `erp_m_merge`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity`
--

CREATE TABLE `activity` (
  `act_id` bigint(20) NOT NULL,
  `activity_id` varchar(15) NOT NULL,
  `activity_type` varchar(200) NOT NULL,
  `activity_describtion` varchar(500) NOT NULL,
  `activity_at` varchar(200) NOT NULL,
  `activity_organization_name` varchar(200) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `participant_count` int(11) NOT NULL,
  `type` varchar(20) NOT NULL,
  `create_create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `activity_cancel` int(11) NOT NULL,
  `activity_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `activity_fees`
--

CREATE TABLE `activity_fees` (
  `actvity_fees_id` bigint(20) NOT NULL,
  `act_id` bigint(20) NOT NULL,
  `total_fees` float NOT NULL,
  `paid_amount` float NOT NULL,
  `remaining_amount` float NOT NULL,
  `payment_status` int(11) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `activity_cancel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `activity_id`
--

CREATE TABLE `activity_id` (
  `atg_activity_id` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `activity_transaction`
--

CREATE TABLE `activity_transaction` (
  `activity_transc_id` bigint(20) NOT NULL,
  `act_id` bigint(20) NOT NULL,
  `currentpay_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `payment_date` date NOT NULL,
  `due_date` date NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `branch_name` varchar(150) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `transc_cancel_status` int(11) NOT NULL,
  `transc_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `apartment`
--

CREATE TABLE `apartment` (
  `apt_id` bigint(20) NOT NULL,
  `apartment_id` varchar(30) NOT NULL,
  `member_name` varchar(200) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `total_amount` float NOT NULL,
  `paid_amount` float NOT NULL,
  `remaining_amount` float NOT NULL,
  `payment_status` int(11) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `apt_cancel` int(11) NOT NULL,
  `apt_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `apartment`
--

INSERT INTO `apartment` (`apt_id`, `apartment_id`, `member_name`, `reason`, `total_amount`, `paid_amount`, `remaining_amount`, `payment_status`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `apt_cancel`, `apt_cancel_reason`) VALUES
(1, 'APT-1000', 'rehan siddiqui', 'ISI Agent', 6000, 5000, 1000, 0, '2020-09-14', 1, '2020-09-14', 1, 1, 'ISI Agent');

-- --------------------------------------------------------

--
-- Table structure for table `apartment_expenditure`
--

CREATE TABLE `apartment_expenditure` (
  `apt_exp_id` bigint(20) NOT NULL,
  `apt_expense _id` varchar(30) NOT NULL,
  `apt_exp_heads` varchar(200) NOT NULL,
  `apt_exp_reason` varchar(500) NOT NULL,
  `apt_total_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `apt_exp_cancel` int(11) NOT NULL,
  `apt_exp_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `apartment_id`
--

CREATE TABLE `apartment_id` (
  `atg_apartment_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `apartment_id`
--

INSERT INTO `apartment_id` (`atg_apartment_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- Table structure for table `apartment_transaction`
--

CREATE TABLE `apartment_transaction` (
  `apt_transc_id` bigint(20) NOT NULL,
  `apt_id` bigint(20) NOT NULL,
  `currentpay_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `branch_name` varchar(150) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `transc_cancel_status` int(11) NOT NULL,
  `transc_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `apartment_transaction`
--

INSERT INTO `apartment_transaction` (`apt_transc_id`, `apt_id`, `currentpay_amount`, `payment_mode`, `account_holder_name`, `bank_name`, `cheque_number`, `ifsc_code`, `branch_name`, `upi_transaction_id`, `transaction_name`, `transaction_mobile`, `google_transaction_id`, `bank_transaction_id`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `transc_cancel_status`, `transc_cancel_reason`) VALUES
(1, 1, 4000, 'Cash', '', '', '', '', '', '', '', '', '', '', '2020-09-14', 1, '2020-09-14', 1, 1, 'Refund'),
(2, 1, 3000, 'Bank Transfer', 'rehan', 'Swiss Bank', 'S-34234', '', 'Capuchino Hills, switzerland', '', '', '', '', '', '2020-09-14', 1, '2020-09-14', 1, 0, ''),
(3, 1, 1000, 'PhonePe', 'Tony Akshay', '', '', '', '', '', '', '8209558546', '', '', '2020-09-14', 1, '2020-09-14', 1, 0, ''),
(4, 1, 1000, 'Paytm', 'Rehan', '', '', '', '', '', '', '8451232513', '', 'TnxID-3324234', '2020-09-14', 1, '2020-09-14', 1, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `atg_expenditure`
--

CREATE TABLE `atg_expenditure` (
  `exp_id` bigint(20) NOT NULL,
  `expense _id` varchar(30) NOT NULL,
  `exp_heads` varchar(200) NOT NULL,
  `exp_reason` varchar(500) NOT NULL,
  `total_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `exp_cancel` int(11) NOT NULL,
  `exp_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `com_id`
--

CREATE TABLE `com_id` (
  `atg_com_id` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `com_project`
--

CREATE TABLE `com_project` (
  `com_id` bigint(20) NOT NULL,
  `com_project_id` varchar(30) NOT NULL,
  `com_first_name` varchar(100) NOT NULL,
  `com_last_name` varchar(100) NOT NULL,
  `com_organisation_name` varchar(200) NOT NULL,
  `com_mobile_no` varchar(13) NOT NULL,
  `com_alternate_mobile` varchar(13) NOT NULL,
  `com_email` varchar(150) NOT NULL,
  `com_gender` varchar(10) NOT NULL,
  `com_dob` varchar(30) NOT NULL,
  `com_project_name` varchar(250) NOT NULL,
  `com_address` text NOT NULL,
  `adhar_number` varchar(14) NOT NULL,
  `adharcard_image` varchar(150) NOT NULL,
  `com_client_image` varchar(50) NOT NULL,
  `com_cancel` int(11) NOT NULL,
  `com_cancel_reason` varchar(400) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `com_project`
--

INSERT INTO `com_project` (`com_id`, `com_project_id`, `com_first_name`, `com_last_name`, `com_organisation_name`, `com_mobile_no`, `com_alternate_mobile`, `com_email`, `com_gender`, `com_dob`, `com_project_name`, `com_address`, `adhar_number`, `adharcard_image`, `com_client_image`, `com_cancel`, `com_cancel_reason`, `created_by`, `create_timestamp`, `last_modify_timestamp`, `last_modify_by`) VALUES
(1, 'ATG-COM-1000', 'super', 'provider', 'sadada', '7066933566', '', 'rb@gmail.com', 'Male', '01-01-1970', 'dsadad', 'IT Park, Nagpur', '345354', '', '', 1, 'ASs', 1, '2020-09-09', '2020-09-14', 1);

-- --------------------------------------------------------

--
-- Table structure for table `com_project_service`
--

CREATE TABLE `com_project_service` (
  `com_service_id` bigint(20) NOT NULL,
  `com_id` bigint(20) NOT NULL,
  `com_service_type` varchar(100) NOT NULL,
  `com_service_desc` varchar(500) NOT NULL,
  `com_total_fees_amount` float NOT NULL,
  `com_paid_amount` float NOT NULL,
  `com_remaining_amount` float NOT NULL,
  `com_payment_status` int(11) NOT NULL,
  `com_cancel` int(11) NOT NULL,
  `com_cancel_reason` varchar(400) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `com_project_service`
--

INSERT INTO `com_project_service` (`com_service_id`, `com_id`, `com_service_type`, `com_service_desc`, `com_total_fees_amount`, `com_paid_amount`, `com_remaining_amount`, `com_payment_status`, `com_cancel`, `com_cancel_reason`, `created_by`, `create_timestamp`, `last_modify_timestamp`, `last_modify_by`) VALUES
(1, 1, 'app', 'fdgdfg', 1000, 500, 500, 0, 1, 'Dhoom Machale\r\n', 1, '2020-09-09', '2020-09-10', 1),
(2, 1, 'Website + App', 'erferwwrew', 6546550, 0, 0, 0, 1, 'dsfdsfsd', 1, '2020-09-09', '2020-09-10', 1),
(3, 1, 'Website + App', 'ewrwrwer', 12323400, 23, -23, 0, 1, ' ', 1, '2020-09-09', '2020-09-14', 1),
(7, 0, 'Webhosting + Domain Name', 'sdfgdsf', 111111000, 0, 0, 0, 0, '', 0, '0000-00-00', '2020-09-10', 1),
(10, 1, 'Webhosting + Domain Name', 'hosting web app', 1000, 0, 1000, 0, 0, '', 1, '2020-09-14', '2020-09-14', 1);

-- --------------------------------------------------------

--
-- Table structure for table `com_transaction`
--

CREATE TABLE `com_transaction` (
  `com_transc_id` bigint(20) NOT NULL,
  `com_service_id` bigint(20) NOT NULL,
  `com_id` bigint(20) NOT NULL,
  `currentpay_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `payment_date` date NOT NULL,
  `due_date` date NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `branch_name` varchar(150) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `transc_cancel_status` int(11) NOT NULL,
  `transc_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `com_transaction`
--

INSERT INTO `com_transaction` (`com_transc_id`, `com_service_id`, `com_id`, `currentpay_amount`, `payment_mode`, `payment_date`, `due_date`, `account_holder_name`, `bank_name`, `cheque_number`, `ifsc_code`, `branch_name`, `upi_transaction_id`, `transaction_name`, `transaction_mobile`, `google_transaction_id`, `bank_transaction_id`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `transc_cancel_status`, `transc_cancel_reason`) VALUES
(3, 1, 1, 55, 'Google Pay', '2020-09-07', '2020-09-07', 'bvcbcbc', '', '', '', '', '', '', '6756765', 'bcvbcv', '', '2020-09-10', 1, '2020-09-10', 1, 0, ''),
(7, 3, 1, 23, 'Paytm', '2020-09-10', '2020-09-10', 'erwrewrw', '', '', '', '', '', '', '3463434634', '', 'ewrewr', '2020-09-10', 1, '2020-09-10', 1, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `degree`
--

CREATE TABLE `degree` (
  `degree_id` int(11) NOT NULL,
  `create_date` date NOT NULL,
  `degree_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `designation`
--

CREATE TABLE `designation` (
  `designation_id` int(11) NOT NULL,
  `create_date` date NOT NULL,
  `designation_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `emp_id` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `mobile_no` varchar(13) NOT NULL,
  `alternate_mobile_no` varchar(13) NOT NULL,
  `email` varchar(150) NOT NULL,
  `joining_date` date NOT NULL,
  `designation_id` int(11) NOT NULL,
  `address` text NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` text NOT NULL,
  `adhar_number` varchar(14) NOT NULL,
  `adharcard_image` varchar(150) NOT NULL,
  `emp_profile_image` varchar(150) NOT NULL,
  `is_active` int(11) NOT NULL,
  `inactive_reason` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `first_name`, `last_name`, `gender`, `dob`, `mobile_no`, `alternate_mobile_no`, `email`, `joining_date`, `designation_id`, `address`, `username`, `password`, `adhar_number`, `adharcard_image`, `emp_profile_image`, `is_active`, `inactive_reason`) VALUES
(1, '2020-09-09', 1, '2020-09-09', 1, 'rohit', 'bhasarkar', '', '2020-09-09', '', '', 'rb@gmail.com', '2020-09-08', 1, '', 'qqq', '111', '', '', '', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `employee_privileges`
--

CREATE TABLE `employee_privileges` (
  `emp_privilage_id` int(11) NOT NULL,
  `emp_id` int(11) NOT NULL,
  `priviege_id` int(11) NOT NULL,
  `all` int(11) NOT NULL,
  `create` int(11) NOT NULL,
  `read` int(11) NOT NULL,
  `update` int(11) NOT NULL,
  `delete` int(11) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `intern`
--

CREATE TABLE `intern` (
  `int_id` bigint(20) NOT NULL,
  `intern_id` varchar(20) NOT NULL,
  `type` varchar(50) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `father_name` varchar(100) NOT NULL,
  `intern_email` varchar(150) NOT NULL,
  `intern_mobile` varchar(13) NOT NULL,
  `alternate_mobile_no` varchar(13) NOT NULL,
  `intern_gender` varchar(10) NOT NULL,
  `inter_DOB` date NOT NULL,
  `intern_city` varchar(100) NOT NULL,
  `intern_address` text NOT NULL,
  `intern_college` varchar(200) NOT NULL,
  `intern_degree` varchar(100) NOT NULL,
  `intern_stream` varchar(30) NOT NULL,
  `inten_year` varchar(30) NOT NULL,
  `batch_time` varchar(30) NOT NULL,
  `percent_ten` float NOT NULL,
  `percent_twelve` float NOT NULL,
  `percent_poly` float NOT NULL,
  `percent_graduation` float NOT NULL,
  `percent_postgraduation` float NOT NULL,
  `intern_technology` varchar(50) NOT NULL,
  `intern_projectname` varchar(200) NOT NULL,
  `intern_placed_at` varchar(200) NOT NULL,
  `intern_image` varchar(150) NOT NULL,
  `adhar_number` varchar(14) NOT NULL,
  `adharcard_image` varchar(150) NOT NULL,
  `intern_cancel` int(11) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `intern_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `intern`
--

INSERT INTO `intern` (`int_id`, `intern_id`, `type`, `first_name`, `last_name`, `father_name`, `intern_email`, `intern_mobile`, `alternate_mobile_no`, `intern_gender`, `inter_DOB`, `intern_city`, `intern_address`, `intern_college`, `intern_degree`, `intern_stream`, `inten_year`, `batch_time`, `percent_ten`, `percent_twelve`, `percent_poly`, `percent_graduation`, `percent_postgraduation`, `intern_technology`, `intern_projectname`, `intern_placed_at`, `intern_image`, `adhar_number`, `adharcard_image`, `intern_cancel`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `intern_cancel_reason`) VALUES
(1, 'test', '', 'Satyam', 'Kuril', 'Shankar', 'satyamkuril@gmail.com', '9595529941', '8788064503', 'Male', '0000-00-00', 'Nagpur', 'Satyam Tyres', 'MIT', 'MCA', 'IT', 'IV Year', '18:15', 66, 65, 60, 63, 63, 'Java', 'ERP', 'Axiom', 'Profile_Satyam_Kuril_20200907181720.png', '9654658715', 'Adhar_Satyam_Kuril_20200907181720.jpg', 0, '0000-00-00', 0, '0000-00-00', 0, ''),
(2, 'ATG-INT-1002', 'Full Time Intern', 'Satyam', 'Kuril', 'Sk', 'satyamkuril@gmail.com', '9595529941', '8788604503', 'Male', '0000-00-00', 'Nagpur', 'Satyam Tyres', 'MIT', 'MCA', 'IT', 'IV Year', '12:00', 66.33, 65, 63, 60, 63, 'Java,C++', 'ERP', 'AXIOM', 'Profile_Satyam_Kuril_20200907195501.png', '6546543215', 'Adhar_Satyam_Kuril_20200907195501.jpg', 1, '0000-00-00', 0, '2020-09-10', 0, 'Test'),
(6, 'ATG-INT-1006', 'Full Time Intern', 'S', 'S', 'K', 'satyamkuril143@gmail.com', '9595529941', '9595529942', 'Male', '2020-09-12', 'Nagpur', 'Satyam Tyres', 'MIT', 'MCA', 'IT', 'IV Year', '10:30', 66, 65, 62, 62, 65, 'Python,C++', 'ERP', 'Axiom', 'Profile_S_S_20200912103013.png', '54165556554', 'Adhar_S_S_20200912103013.png', 0, '2020-09-12', 0, '2020-09-12', 0, ''),
(7, 'ATG-INT-1007', 'Full Time Intern', 'Nick', 'Wotson', 'Mike', 'nick@gmail.com', '9595529941', '', 'Male', '2020-09-12', 'Nagpur', 'Nag', 'MIT', 'MCA', 'CSE', 'IV Year', '16:51', 66, 65, 50, 60, 65, 'Python,C_Language', 'ERP', 'AXIOM', 'Profile_Nick_Wotson_20200912165808.png', '855226565', 'Adhar_Nick_Wotson_20200912165808.jpg', 0, '2020-09-12', 0, '0000-00-00', 0, ''),
(8, 'ATG-INT-1008', 'Full Time Intern', 'S', 'K', 'S', 'sk@gmail.com', '9595955241', '', 'Male', '2020-09-12', 'Nagpur', 'Satyam Tyres', 'MIT', 'B.Tech', 'IT', 'II Year', '19:19', 65, 66, 45, 84, 65, 'Python,C++', 'Axiom ERP', 'Axiom', 'Profile_S_K_20200912192150.png', '654654654', 'Adhar_S_K_20200912192150.jpg', 0, '2020-09-12', 1, '2020-09-12', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `intern_fees`
--

CREATE TABLE `intern_fees` (
  `intern_fees_id` bigint(20) NOT NULL,
  `intern_id` bigint(20) NOT NULL,
  `total_fees` float NOT NULL,
  `paid_amount` float NOT NULL,
  `remaining_amount` float NOT NULL,
  `payment_status` int(11) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `intern_cancel` int(11) NOT NULL,
  `cancel_reason` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `intern_fees`
--

INSERT INTO `intern_fees` (`intern_fees_id`, `intern_id`, `total_fees`, `paid_amount`, `remaining_amount`, `payment_status`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `intern_cancel`, `cancel_reason`) VALUES
(1, 5, 10000, 5000, 5000, 0, '2020-09-10', 0, '2020-09-11', 0, 0, ''),
(2, 1, 5000, 0, 0, 0, '2020-09-11', 0, '0000-00-00', 0, 0, ''),
(3, 6, 12000, 2000, 10000, 0, '2020-09-12', 0, '2020-09-12', 0, 0, ''),
(4, 2, 6000, 2000, 4000, 0, '2020-09-12', 0, '2020-09-12', 0, 0, ''),
(5, 8, 6000, 500, 5500, 0, '2020-09-12', 1, '2020-09-12', 1, 1, 'Test');

-- --------------------------------------------------------

--
-- Table structure for table `intern_id`
--

CREATE TABLE `intern_id` (
  `atg_intern_id` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `intern_id`
--

INSERT INTO `intern_id` (`atg_intern_id`) VALUES
(1008);

-- --------------------------------------------------------

--
-- Table structure for table `intern_transaction`
--

CREATE TABLE `intern_transaction` (
  `intern_transc_id` bigint(20) NOT NULL,
  `intern_id` bigint(20) NOT NULL,
  `currentpay_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `payment_date` date NOT NULL,
  `due_date` date NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `branch_name` varchar(150) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `transc_cancel_status` int(11) NOT NULL,
  `transc_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `intern_transaction`
--

INSERT INTO `intern_transaction` (`intern_transc_id`, `intern_id`, `currentpay_amount`, `payment_mode`, `payment_date`, `due_date`, `account_holder_name`, `bank_name`, `cheque_number`, `branch_name`, `ifsc_code`, `upi_transaction_id`, `transaction_name`, `transaction_mobile`, `google_transaction_id`, `bank_transaction_id`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `transc_cancel_status`, `transc_cancel_reason`) VALUES
(1, 5, 1000, 'cash', '2020-09-11', '0000-00-00', '', '', '', '', '', '', '', '', '', '', '2020-09-11', 0, '0000-00-00', 0, 0, ''),
(2, 5, 1000, 'bank', '2020-09-11', '2020-09-12', 'Satyam', 'PNB', '875425', 'GB', 'PNB8585', '', '', '', '', '', '2020-09-11', 0, '0000-00-00', 0, 0, ''),
(3, 5, 1000, 'phonepe', '2020-09-11', '0000-00-00', '', '', '', '', '', 'PonePe123', 'Satyam', '9595529941', '', '', '2020-09-11', 0, '2020-09-11', 0, 1, 'Test'),
(4, 5, 1000, 'googlepe', '2020-09-11', '0000-00-00', '', '', '', '', '', '', 'Satyam', '9595529941', 'UPI123', '', '2020-09-11', 0, '0000-00-00', 0, 0, ''),
(5, 5, 1000, 'paytm', '2020-09-11', '0000-00-00', '', '', '', '', '', '', 'Satyam', '9595529941', '', 'PAYTM', '2020-09-11', 0, '0000-00-00', 0, 0, ''),
(6, 5, 1000, 'googlepe', '2020-09-11', '0000-00-00', '', '', '', '', '', 'Upi123', 'Satyam', '9595529941', 'Upi123', '', '2020-09-11', 0, '2020-09-11', 0, 0, ''),
(8, 6, 2000, 'cash', '2020-09-12', '0000-00-00', '', '', '', '', '', '', '', '', '', '', '2020-09-12', 0, '0000-00-00', 0, 0, ''),
(9, 6, 1000, 'phonepe', '2020-09-12', '0000-00-00', '', '', '', '', '', 'UPI123', 'Satyam', '9595525542', '', '', '2020-09-12', 0, '2020-09-12', 0, 1, ''),
(10, 2, 1000, 'cash', '2020-09-12', '0000-00-00', '', '', '', '', '', '', '', '', '', '', '2020-09-12', 0, '0000-00-00', 0, 0, ''),
(11, 2, 1000, 'bank', '2020-09-12', '2020-09-12', 'Satyam', 'jhdbc', '684754', 'fkbv', 'smkbfv5', '', '', '', '', '', '2020-09-12', 0, '0000-00-00', 0, 0, ''),
(12, 8, 500, 'cash', '2020-09-12', '0000-00-00', '', '', '', '', '', '', '', '', '', '', '2020-09-12', 1, '0000-00-00', 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `pg_id`
--

CREATE TABLE `pg_id` (
  `atg_pg_id` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pg_project`
--

CREATE TABLE `pg_project` (
  `pg_id` bigint(20) NOT NULL,
  `pg_project_id` varchar(30) NOT NULL,
  `pg_first_name` varchar(100) NOT NULL,
  `pg_last_name` varchar(100) NOT NULL,
  `pg_email` varchar(150) NOT NULL,
  `pg_mobile` varchar(13) NOT NULL,
  `pg_altenate_mobile` varchar(13) NOT NULL,
  `pg_dob` varchar(15) NOT NULL,
  `pg_gender` varchar(10) NOT NULL,
  `pg_address` text NOT NULL,
  `pg_college_name` varchar(100) NOT NULL,
  `pg_degree` varchar(100) NOT NULL,
  `pg_stream` varchar(100) NOT NULL,
  `pg_year` varchar(10) NOT NULL,
  `pg_tehnology` varchar(100) NOT NULL,
  `pg_project_name` varchar(400) NOT NULL,
  `adhar_number` varchar(14) NOT NULL,
  `adharcard_image` varchar(150) NOT NULL,
  `pg_cancel` int(11) NOT NULL,
  `pg_cancel_reason` varchar(400) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pg_project_fees`
--

CREATE TABLE `pg_project_fees` (
  `pg_fees_id` bigint(20) NOT NULL,
  `pg_id` bigint(20) NOT NULL,
  `total_fees_amount` float NOT NULL,
  `paid_amount` float NOT NULL,
  `remaining_amount` float NOT NULL,
  `payment_status` int(11) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `pg_cancel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pg_transaction`
--

CREATE TABLE `pg_transaction` (
  `pg_transc_id` bigint(20) NOT NULL,
  `pg_id` bigint(20) NOT NULL,
  `currentpay_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `branch_name` varchar(150) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `transc_cancel_status` int(11) NOT NULL,
  `transc_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `phd_id`
--

CREATE TABLE `phd_id` (
  `atg_phd_id` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `phd_id`
--

INSERT INTO `phd_id` (`atg_phd_id`) VALUES
(1001);

-- --------------------------------------------------------

--
-- Table structure for table `phd_module`
--

CREATE TABLE `phd_module` (
  `phd_module_id` bigint(20) NOT NULL,
  `phd_id` bigint(20) NOT NULL,
  `phd_project_id` varchar(30) NOT NULL,
  `phd_module_name` varchar(200) NOT NULL,
  `phd_module_desc` varchar(500) NOT NULL,
  `phd_technology` varchar(100) NOT NULL,
  `phd_total_fees_amount` float NOT NULL,
  `phd_paid_amount` float NOT NULL,
  `phd_remaining_amount` float NOT NULL,
  `phd_payment_status` int(11) NOT NULL,
  `phd_cancel` int(11) NOT NULL,
  `phd_cancel_reason` varchar(400) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `phd_module`
--

INSERT INTO `phd_module` (`phd_module_id`, `phd_id`, `phd_project_id`, `phd_module_name`, `phd_module_desc`, `phd_technology`, `phd_total_fees_amount`, `phd_paid_amount`, `phd_remaining_amount`, `phd_payment_status`, `phd_cancel`, `phd_cancel_reason`, `created_by`, `create_timestamp`, `last_modify_timestamp`, `last_modify_by`) VALUES
(1, 1, '', 'website', 'website upload on server', 'Python,C++', 60, 15, 45, 0, 0, '', 0, '2020-09-17', '0000-00-00', 0),
(2, 1, '', 'App', 'Website application', 'Java,MySqli', 100, 0, 100, 0, 0, '', 0, '2020-09-17', '0000-00-00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `phd_project`
--

CREATE TABLE `phd_project` (
  `phd_id` bigint(20) NOT NULL,
  `phd_project_id` varchar(30) NOT NULL,
  `phd_first_name` varchar(100) NOT NULL,
  `phd_last_name` varchar(100) NOT NULL,
  `phd_email` varchar(150) NOT NULL,
  `phd_mobile_no` varchar(13) NOT NULL,
  `phd_alternate_mobile` varchar(13) NOT NULL,
  `phd_gender` varchar(10) NOT NULL,
  `phd_dob` varchar(30) NOT NULL,
  `phd_address` text NOT NULL,
  `phd_project_name` varchar(400) NOT NULL,
  `phd_domain_name` varchar(200) NOT NULL,
  `adhar_number` varchar(14) NOT NULL,
  `adharcard_image` varchar(150) NOT NULL,
  `profile_img` varchar(150) NOT NULL,
  `phd_cancel` int(11) NOT NULL,
  `phd_cancel_reason` varchar(400) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `phd_project`
--

INSERT INTO `phd_project` (`phd_id`, `phd_project_id`, `phd_first_name`, `phd_last_name`, `phd_email`, `phd_mobile_no`, `phd_alternate_mobile`, `phd_gender`, `phd_dob`, `phd_address`, `phd_project_name`, `phd_domain_name`, `adhar_number`, `adharcard_image`, `profile_img`, `phd_cancel`, `phd_cancel_reason`, `created_by`, `create_timestamp`, `last_modify_timestamp`, `last_modify_by`) VALUES
(1, 'ATG-PHD-1001', 'shubham', 'kamble', 'shubhamkamble@gmail.com', '9595936381', '885556666000', 'Male', 'Thursday 17 September 2020', 'HGT', 'Axiom ERP', 'axiomerp.com', '5550000000', 'addhar_shubham_kamble_20200917114057.png', 'shubham_kamble_20200917114057.png', 0, '', 0, '2020-09-17', '0000-00-00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `phd_transaction`
--

CREATE TABLE `phd_transaction` (
  `phd_transc_id` bigint(20) NOT NULL,
  `phd_id` bigint(20) NOT NULL,
  `phd_module_id` bigint(20) NOT NULL,
  `currentpay_amount` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `payment_date` date NOT NULL,
  `due_date` date NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `branch_name` varchar(150) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `create_timestamp` date NOT NULL,
  `created_by` int(11) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` int(11) NOT NULL,
  `transc_cancel_status` int(11) NOT NULL,
  `transc_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `phd_transaction`
--

INSERT INTO `phd_transaction` (`phd_transc_id`, `phd_id`, `phd_module_id`, `currentpay_amount`, `payment_mode`, `payment_date`, `due_date`, `account_holder_name`, `bank_name`, `cheque_number`, `ifsc_code`, `branch_name`, `upi_transaction_id`, `transaction_name`, `transaction_mobile`, `google_transaction_id`, `bank_transaction_id`, `create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `transc_cancel_status`, `transc_cancel_reason`) VALUES
(1, 1, 1, 10, 'cash', '2020-09-17', '0000-00-00', '', '', '', '', '', '', '', '', '', '', '2020-09-17', 0, '0000-00-00', 0, 0, ''),
(2, 1, 1, 5, 'googlepe', '2020-09-17', '0000-00-00', 'shubham kamble', '', '', '', '', 'upi5550000', '', '95959595959', 'ggltrans00555', '', '2020-09-17', 0, '0000-00-00', 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `privileges`
--

CREATE TABLE `privileges` (
  `priviege_id` int(11) NOT NULL,
  `module_name` varchar(250) NOT NULL,
  `all` int(11) NOT NULL,
  `create` int(11) NOT NULL,
  `read` int(11) NOT NULL,
  `update` int(11) NOT NULL,
  `delete` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sponsor_intern`
--

CREATE TABLE `sponsor_intern` (
  `si_int_id` bigint(20) NOT NULL,
  `si_intern_id` varchar(20) NOT NULL,
  `si_type` varchar(50) NOT NULL,
  `si_first_name` varchar(100) NOT NULL,
  `si_last_name` varchar(100) NOT NULL,
  `si_father_name` varchar(100) NOT NULL,
  `si_email` varchar(150) NOT NULL,
  `si_mobile` varchar(13) NOT NULL,
  `si_parent_contact` varchar(13) NOT NULL,
  `si_gender` varchar(10) NOT NULL,
  `si_dob` date NOT NULL,
  `si_city` varchar(100) NOT NULL,
  `si_address` text NOT NULL,
  `si_college` varchar(200) NOT NULL,
  `si_degree` varchar(100) NOT NULL,
  `si_stream` varchar(30) NOT NULL,
  `si_year` varchar(30) NOT NULL,
  `batch_time` varchar(30) NOT NULL,
  `percent_ten` float NOT NULL,
  `percent_twelve` float NOT NULL,
  `percent_poly` float NOT NULL,
  `percent_graduation` float NOT NULL,
  `percent_postgraduation` float NOT NULL,
  `si_technology` varchar(50) NOT NULL,
  `si_projectname` varchar(200) NOT NULL,
  `si_placed_at` varchar(200) NOT NULL,
  `si_image` varchar(150) NOT NULL,
  `adhar_number` varchar(14) NOT NULL,
  `adharcard_image` varchar(150) NOT NULL,
  `profile_image` varchar(150) NOT NULL,
  `create_create_timestamp` date NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `si_cancel` int(11) NOT NULL,
  `si_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sponsor_intern`
--

INSERT INTO `sponsor_intern` (`si_int_id`, `si_intern_id`, `si_type`, `si_first_name`, `si_last_name`, `si_father_name`, `si_email`, `si_mobile`, `si_parent_contact`, `si_gender`, `si_dob`, `si_city`, `si_address`, `si_college`, `si_degree`, `si_stream`, `si_year`, `batch_time`, `percent_ten`, `percent_twelve`, `percent_poly`, `percent_graduation`, `percent_postgraduation`, `si_technology`, `si_projectname`, `si_placed_at`, `si_image`, `adhar_number`, `adharcard_image`, `profile_image`, `create_create_timestamp`, `created_by`, `last_modify_timestamp`, `last_modify_by`, `si_cancel`, `si_cancel_reason`) VALUES
(1, 'ATG-SP-INT-1001', 'sponser', 'John', 'Hoffs', 'Stefen', 'hoffs@gmail.com', '869656565', '', 'Male', '2020-09-18', 'New York', 'West, New York', 'Institute', '20', 'IT', 'III Year', '', 86, 75, 78, 56, 86, 'JS_Script,Java,Jquery', 'ERP', 'Axiom', '', '8451515151515', 'addhar_John_Hoffs_20200918171125.jpeg', 'John_Hoffs_20200918171125.png', '2020-09-18', 0, '0000-00-00', 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `sp_intern_id`
--

CREATE TABLE `sp_intern_id` (
  `atg_sp_intern_id` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sp_intern_id`
--

INSERT INTO `sp_intern_id` (`atg_sp_intern_id`) VALUES
(1001);

-- --------------------------------------------------------

--
-- Table structure for table `stream`
--

CREATE TABLE `stream` (
  `stream_id` int(11) NOT NULL,
  `create_date` date NOT NULL,
  `stream_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `technology`
--

CREATE TABLE `technology` (
  `technology_id` int(11) NOT NULL,
  `create_date` date NOT NULL,
  `technology_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ug_id`
--

CREATE TABLE `ug_id` (
  `atg_ug_id` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ug_member`
--

CREATE TABLE `ug_member` (
  `member_id` bigint(20) NOT NULL,
  `ug_id` bigint(20) NOT NULL,
  `ug_first_name` varchar(100) NOT NULL,
  `ug_last_name` varchar(100) NOT NULL,
  `ug_fathername` varchar(100) NOT NULL,
  `ug_mobile_no` varchar(13) NOT NULL,
  `ug_alternate_mobile` varchar(13) NOT NULL,
  `ug_gender` varchar(10) NOT NULL,
  `ug_dob` varchar(15) NOT NULL,
  `ug_intern_address` text NOT NULL,
  `ug_intern_image` varchar(50) NOT NULL,
  `adhar_number` varchar(14) NOT NULL,
  `adharcard_image` varchar(150) NOT NULL,
  `ug_cancel_reg` int(11) NOT NULL,
  `ug_cancel_reason` varchar(400) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ug_member_fees`
--

CREATE TABLE `ug_member_fees` (
  `ug_fees_id` bigint(20) NOT NULL,
  `ug_id` bigint(20) NOT NULL,
  `member_id` bigint(20) NOT NULL,
  `ug_reg_type` varchar(50) NOT NULL,
  `total_fees_amount` float NOT NULL,
  `paid_amount` float NOT NULL,
  `remaining_amount` float NOT NULL,
  `payment_status` int(11) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `ug_cancel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ug_project`
--

CREATE TABLE `ug_project` (
  `ug_id` bigint(20) NOT NULL,
  `ug_project_id` varchar(30) NOT NULL,
  `ug_projectdate` date NOT NULL,
  `ug_reg_type` varchar(50) NOT NULL,
  `ug_college_name` varchar(200) NOT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `ug_stream` varchar(100) NOT NULL,
  `ug_year` varchar(10) NOT NULL,
  `ug_tehnology` varchar(100) NOT NULL,
  `ug_projectname` varchar(400) NOT NULL,
  `ug_total_fees` float NOT NULL,
  `ug_cancel` int(11) NOT NULL,
  `ug_cancel_reason` varchar(400) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ug_transaction`
--

CREATE TABLE `ug_transaction` (
  `ug_transc_id` bigint(20) NOT NULL,
  `ug_id` bigint(20) NOT NULL,
  `ug_fees_id` bigint(20) NOT NULL,
  `member_id` bigint(20) NOT NULL,
  `ug_reg_type` varchar(50) NOT NULL,
  `current_pay` float NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `payment_date` date NOT NULL,
  `due_date` date NOT NULL,
  `account_holder_name` varchar(150) NOT NULL,
  `bank_name` varchar(150) NOT NULL,
  `cheque_number` varchar(20) NOT NULL,
  `ifsc_code` varchar(20) NOT NULL,
  `branch_name` varchar(150) NOT NULL,
  `upi_transaction_id` varchar(25) NOT NULL,
  `transaction_name` varchar(150) NOT NULL,
  `transaction_mobile` varchar(13) NOT NULL,
  `google_transaction_id` varchar(25) NOT NULL,
  `bank_transaction_id` varchar(25) NOT NULL,
  `created_by` bigint(20) NOT NULL,
  `create_timestamp` date NOT NULL,
  `last_modify_timestamp` date NOT NULL,
  `last_modify_by` bigint(20) NOT NULL,
  `transc_cancel_status` int(11) NOT NULL,
  `transc_cancel_reason` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity`
--
ALTER TABLE `activity`
  ADD PRIMARY KEY (`act_id`);

--
-- Indexes for table `activity_fees`
--
ALTER TABLE `activity_fees`
  ADD PRIMARY KEY (`actvity_fees_id`);

--
-- Indexes for table `activity_transaction`
--
ALTER TABLE `activity_transaction`
  ADD PRIMARY KEY (`activity_transc_id`);

--
-- Indexes for table `apartment`
--
ALTER TABLE `apartment`
  ADD PRIMARY KEY (`apt_id`);

--
-- Indexes for table `apartment_expenditure`
--
ALTER TABLE `apartment_expenditure`
  ADD PRIMARY KEY (`apt_exp_id`);

--
-- Indexes for table `apartment_transaction`
--
ALTER TABLE `apartment_transaction`
  ADD PRIMARY KEY (`apt_transc_id`);

--
-- Indexes for table `atg_expenditure`
--
ALTER TABLE `atg_expenditure`
  ADD PRIMARY KEY (`exp_id`);

--
-- Indexes for table `com_project`
--
ALTER TABLE `com_project`
  ADD PRIMARY KEY (`com_id`);

--
-- Indexes for table `com_project_service`
--
ALTER TABLE `com_project_service`
  ADD PRIMARY KEY (`com_service_id`);

--
-- Indexes for table `com_transaction`
--
ALTER TABLE `com_transaction`
  ADD PRIMARY KEY (`com_transc_id`);

--
-- Indexes for table `degree`
--
ALTER TABLE `degree`
  ADD PRIMARY KEY (`degree_id`);

--
-- Indexes for table `designation`
--
ALTER TABLE `designation`
  ADD PRIMARY KEY (`designation_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `employee_privileges`
--
ALTER TABLE `employee_privileges`
  ADD PRIMARY KEY (`emp_privilage_id`);

--
-- Indexes for table `intern`
--
ALTER TABLE `intern`
  ADD PRIMARY KEY (`int_id`);

--
-- Indexes for table `intern_fees`
--
ALTER TABLE `intern_fees`
  ADD PRIMARY KEY (`intern_fees_id`);

--
-- Indexes for table `intern_transaction`
--
ALTER TABLE `intern_transaction`
  ADD PRIMARY KEY (`intern_transc_id`);

--
-- Indexes for table `pg_project`
--
ALTER TABLE `pg_project`
  ADD PRIMARY KEY (`pg_id`);

--
-- Indexes for table `pg_project_fees`
--
ALTER TABLE `pg_project_fees`
  ADD PRIMARY KEY (`pg_fees_id`);

--
-- Indexes for table `pg_transaction`
--
ALTER TABLE `pg_transaction`
  ADD PRIMARY KEY (`pg_transc_id`);

--
-- Indexes for table `phd_module`
--
ALTER TABLE `phd_module`
  ADD PRIMARY KEY (`phd_module_id`);

--
-- Indexes for table `phd_project`
--
ALTER TABLE `phd_project`
  ADD PRIMARY KEY (`phd_id`);

--
-- Indexes for table `phd_transaction`
--
ALTER TABLE `phd_transaction`
  ADD PRIMARY KEY (`phd_transc_id`);

--
-- Indexes for table `privileges`
--
ALTER TABLE `privileges`
  ADD PRIMARY KEY (`priviege_id`);

--
-- Indexes for table `sponsor_intern`
--
ALTER TABLE `sponsor_intern`
  ADD PRIMARY KEY (`si_int_id`);

--
-- Indexes for table `stream`
--
ALTER TABLE `stream`
  ADD PRIMARY KEY (`stream_id`);

--
-- Indexes for table `technology`
--
ALTER TABLE `technology`
  ADD PRIMARY KEY (`technology_id`);

--
-- Indexes for table `ug_member`
--
ALTER TABLE `ug_member`
  ADD PRIMARY KEY (`member_id`);

--
-- Indexes for table `ug_member_fees`
--
ALTER TABLE `ug_member_fees`
  ADD PRIMARY KEY (`ug_fees_id`);

--
-- Indexes for table `ug_project`
--
ALTER TABLE `ug_project`
  ADD PRIMARY KEY (`ug_id`);

--
-- Indexes for table `ug_transaction`
--
ALTER TABLE `ug_transaction`
  ADD PRIMARY KEY (`ug_transc_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity`
--
ALTER TABLE `activity`
  MODIFY `act_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `activity_fees`
--
ALTER TABLE `activity_fees`
  MODIFY `actvity_fees_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `activity_transaction`
--
ALTER TABLE `activity_transaction`
  MODIFY `activity_transc_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `apartment`
--
ALTER TABLE `apartment`
  MODIFY `apt_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `apartment_expenditure`
--
ALTER TABLE `apartment_expenditure`
  MODIFY `apt_exp_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `apartment_transaction`
--
ALTER TABLE `apartment_transaction`
  MODIFY `apt_transc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `atg_expenditure`
--
ALTER TABLE `atg_expenditure`
  MODIFY `exp_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `com_project`
--
ALTER TABLE `com_project`
  MODIFY `com_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `com_project_service`
--
ALTER TABLE `com_project_service`
  MODIFY `com_service_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `com_transaction`
--
ALTER TABLE `com_transaction`
  MODIFY `com_transc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `degree`
--
ALTER TABLE `degree`
  MODIFY `degree_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `designation`
--
ALTER TABLE `designation`
  MODIFY `designation_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `emp_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `employee_privileges`
--
ALTER TABLE `employee_privileges`
  MODIFY `emp_privilage_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `intern`
--
ALTER TABLE `intern`
  MODIFY `int_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `intern_fees`
--
ALTER TABLE `intern_fees`
  MODIFY `intern_fees_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `intern_transaction`
--
ALTER TABLE `intern_transaction`
  MODIFY `intern_transc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `pg_project`
--
ALTER TABLE `pg_project`
  MODIFY `pg_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pg_project_fees`
--
ALTER TABLE `pg_project_fees`
  MODIFY `pg_fees_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pg_transaction`
--
ALTER TABLE `pg_transaction`
  MODIFY `pg_transc_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `phd_module`
--
ALTER TABLE `phd_module`
  MODIFY `phd_module_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `phd_project`
--
ALTER TABLE `phd_project`
  MODIFY `phd_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `phd_transaction`
--
ALTER TABLE `phd_transaction`
  MODIFY `phd_transc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `privileges`
--
ALTER TABLE `privileges`
  MODIFY `priviege_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sponsor_intern`
--
ALTER TABLE `sponsor_intern`
  MODIFY `si_int_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `stream`
--
ALTER TABLE `stream`
  MODIFY `stream_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `technology`
--
ALTER TABLE `technology`
  MODIFY `technology_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ug_member`
--
ALTER TABLE `ug_member`
  MODIFY `member_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ug_member_fees`
--
ALTER TABLE `ug_member_fees`
  MODIFY `ug_fees_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ug_project`
--
ALTER TABLE `ug_project`
  MODIFY `ug_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ug_transaction`
--
ALTER TABLE `ug_transaction`
  MODIFY `ug_transc_id` bigint(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

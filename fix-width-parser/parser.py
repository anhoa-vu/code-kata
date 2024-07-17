import csv
import argparse

def read_spec_file(spec_file, encoding):
    try:
        with open(spec_file, 'r', encoding=encoding, errors='replace') as file:
            spec = [line.strip().split(':') for line in file]
            fields = [field for field, _ in spec]
            lengths = [int(length) for _, length in spec]
        return fields, lengths
    except Exception as e:
        print(f"Error reading specification file: {e}")
        raise

def parse_fixed_width_file(data_file, lengths, encoding):
    total_length = sum(lengths)
    #check if the line length matched with total spec length
    try:
        with open(data_file, 'r', encoding=encoding, errors='replace') as file:
            lines = file.readlines()
        
        for line in lines:
            if len(line.strip()) != total_length:
                raise ValueError(f"Line length {len(line.strip())} does not match total spec length {total_length}")
        
        parsed_data = []
        for line in lines:
            start = 0
            parsed_line = []
            for length in lengths:
                parsed_line.append(line[start:start+length].strip())
                start += length
            parsed_data.append(parsed_line)
        return parsed_data
    except Exception as e:
        print(f"Error reading fixed-width data file: {e}")
        raise

def write_csv_file(output_file, fields, parsed_data, encoding):
    try:
        with open(output_file, 'w', newline='', encoding=encoding, errors='replace') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(parsed_data)
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse fixed-width file and generate CSV file.')
    parser.add_argument('spec_file', help='Specification file')
    parser.add_argument('data_file', help='Fixed-width data file')
    parser.add_argument('output_file', help='Output CSV file')
    parser.add_argument('--encoding', default='utf-8', help='File encoding (default: utf-8)')
    
    args = parser.parse_args()
    
    try:
        fields, lengths = read_spec_file(args.spec_file, args.encoding)
        parsed_data = parse_fixed_width_file(args.data_file, lengths, args.encoding)
        write_csv_file(args.output_file, fields, parsed_data, args.encoding)
    except Exception as e:
        print(f"An error occurred: {e}")

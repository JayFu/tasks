from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('sumsum1.html')

@app.route('/submit', methods = ['GET'])
def findMedianSortedArrays():
        num1 = request.args.get('num1')
        nums1 = num1.split(',')
        num2 = request.args.get('num2')
        nums2 = num1.split(',')
        m = len(nums1)
        n = len(nums2)
        
        outputnums = []
        num2 = 0
        
        if (m + n) % 2 == 0:
            num2 = (m + n) // 2
            num1 = num2 - 1
        else:
            num1 = (m + n) // 2
        
        a = 0
        b = 0
        
        for i in range(0 , ((m + n) // 2 + 1)):
            if a >= m:
                outputnums.append(nums2[b])
                b += 1
            elif b >= n:
                outputnums.append(nums1[a])
                a += 1
            elif nums1[a] > nums2[b]:
                outputnums.append(nums2[b])
                b += 1
            else:
                outputnums.append(nums1[a])
                a += 1
        
        if num2 == 0: outcc =  outputnums[num1]
        else : outcc = (float(outputnums[num1] + outputnums[num2])) / 2

        return render_template( 'endingg.html', ending = outcc)

if __name__ == '__main__':
    app.run()